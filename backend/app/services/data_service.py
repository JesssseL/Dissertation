import pymongo
from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
import bcrypt
from app.config import settings

cluster=MongoClient(settings.db_connection)
db=cluster["Dis"]
collection=db["UserAccounts"]

# Ensures no duplicate emails can be inserted
collection.create_index([("email", ASCENDING)], unique=True)

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")

def get_verified_account(email: str, password: str):
    email = email.lower().strip()
    account = collection.find_one({"email": email})
    if not account:
        return False

    password_valid = bcrypt.checkpw(
        password.encode("utf-8"),
        account["password_hash"].encode("utf-8")
    )
    if not password_valid:
        return False

    return account

def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    )


def add_or_get_account_db(email: str, password: str):
    email = email.lower().strip()

    existing_account = collection.find_one({"email": email})

    # if account exists, try sign in
    if existing_account:
        if verify_password(password, existing_account["password_hash"]):
            return {
                "success": True,
                "message": "Signed in successfully",
                "mode": "login",
                "account_products": existing_account.get("account_products", [])
            }

        return {
            "success": False,
            "message": "Incorrect password"
        }

    # no account exists, create one
    account = {
        "email": email,
        "password_hash": hash_password(password),
        "account_products": []
    }

    try:
        result = collection.insert_one(account)

        return {
            "success": True,
            "message": "Account created successfully",
            "mode": "register",
            "inserted_id": str(result.inserted_id),
            "account_products": []
        }

    except DuplicateKeyError:
        return {
            "success": False,
            "message": "Account already exists"
        }

def add_account_products_to_db(email: str, password: str, product):
    account = get_verified_account(email, password)
    
    if not account:
        return {
            "success": False,
            "message": "Account validation failed"
        }

    result = collection.update_one(
        {"_id": account["_id"]},
        {"$push": {"account_products": product.model_dump()}}
    )

    return {
        "success": True,
        "message": "Product added",
        "modified_count": result.modified_count
    }

def get_account_products_from_db(email: str, password: str):
    account = get_verified_account(email, password)
    
    if not account:
        return {
            "success": False,
            "message": "Account validation failed"
        }

    return {
        "success": True,
        "account_products": account.get("account_products", [])
    }