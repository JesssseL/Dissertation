<template>
    <div   
        v-if="open" 
        ref="burgerMenu"
        class="burger-open"
    >
        <div class="burger-close">
            <AppButton
                leftIcon="close"
                theme="tertiary"
                @click="closeMenu"
            />
        </div>

        <span class="burger-title"> 
            Ai Shopping
        </span>

        <AppButton
            leftIcon="search"
            text="Product Search"
            :fullWidth="true"
            :theme="menuRoute === 'search' ? 'secondary' : 'ghost'"
            @click="goTo('Home')"
        />
        <AppButton
            leftIcon="folder_open"
            text="Saved Products"
            :fullWidth="true"
            :theme="menuRoute === 'saved-products' ? 'secondary' : 'ghost'"
            @click="goTo('SavedProducts')"
        />
        <AppButton
            leftIcon="person"
            text="Account"
            :fullWidth="true"
            :theme="menuRoute === 'account' ? 'secondary' : 'ghost'"
            @click="goTo('Account')"
        />

        <div class="burger-sign-ons">
            <AppButton
                v-if="loggedIn"
                leftIcon="logout"
                text="Log out"
                :fullWidth="true"
                theme="primary"
                @click="closeMenu"
            />
            <AppButton
                v-else
                leftIcon="login"
                text="Log in"
                :fullWidth="true"
                theme="primary"
                @click="closeMenu"
            />
        </div>
    </div>
    <AppButton
        v-else
        class="burger-button"
        leftIcon="menu"
        theme="tertiary"
        @click="openMenu"
    />
</template>

<script>
import AppButton from '@/elements/AppButton.vue';

export default {
  name: "BurgerMenu",
  props: {
    currentRoute: {
        type: String,
        required: true
    }
  },
  components: {
    AppButton
  },
  data() {
    return {
        open: false
    }
  },
  watch: {},
  computed: {
    menuRoute() {
        if (this.currentRoute == 'saved-products') {
            return 'saved-products'
        } else if (this.currentRoute == 'account') {
            return 'account'
        } else {
            return 'search'
        }
    }
  },
  mounted() {
    document.addEventListener('click', this.handleOutsideClick, true)
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleOutsideClick, true)
  },
  methods: {
    openMenu() {
        this.open = true
    },
    closeMenu() {
        this.open = false
    },
    goTo(routeName) {
        this.$router.push({ name: routeName })
        this.closeMenu()
    },
    handleOutsideClick(event) {
        if (!this.open) return

        const menu = this.$refs.burgerMenu
        if (menu && !menu.contains(event.target)) {
            this.closeMenu()
        }
    }
  },
};
</script>

<style scoped>
.burger-button {
    position: absolute;
    left: var(--padding-large);
    top: var(--padding-large);
}
.burger-open {
    position: absolute;
    left: 0;
    top: 0;
    width: 300px;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: var(--gap);
    padding: var(--padding-large);
    background: var(--background-gradient);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-small);
    z-index: var(--above-all);
}
.burger-close {
    display: flex;
    justify-content: end;
}
.burger-sign-ons {
    margin-top: auto;
}
.burger-title {
    font-family: var(--font-secondary);
    font-size: 2rem;
    font-weight: 600;
    line-height: 1;
    letter-spacing: 0.02em;
    padding: var(--padding-large);
}
button {
    justify-content: start;
    gap: calc(var(--gap) * 2);
}
</style>