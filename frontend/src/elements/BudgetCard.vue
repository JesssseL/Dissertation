<template>
    <div class="budget-card">
        <input 
            type="radio" 
            name="budget" 
            id="budget1"
            @change="select"
            :checked="selected"
        >
        <label for="budget1" class="card">
            <div class="icon"> {{icon}} </div>
            <h3 class="label"> {{label}} </h3>
            <p class="budget-text"> {{getBudgetText()}} </p>
        </label>
    </div>
</template>

<script>
    export default {
        name: "BudgetCard",
        props: {
            icon: {
                type: String,
                default: "",
            },
            label: {
                type: String,
                default: "",
            },
            type: {
                type: String,
                default: "low",
            },
            min: {
                type: Number,
                default: 0
            },
            max: {
                type: Number,
                default: 100
            },
            selected: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            getBudgetText() {
                switch (this.type) {
                    case 'low':
                        return `Under £${this.max}`

                    case 'high':
                        return `Over £${this.min}`

                    case 'mid':
                        return `£${this.min} - £${this.max}`

                    default:
                        return ''
                }
            },
            select() {
                this.$emit("select", {
                    min: this.min,
                    max: this.max,
                    type: this.type
                });
            }
        },
    }
</script>

<style scoped>
.icon {
  font-size: 3rem;
  margin-bottom: 0.5rem;
  color: var(--primary);
}
.label {
  font-size: 1.2rem;
  font-weight: 600;
}
.budget-card {
    padding: 40px 0;
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    justify-content: center;
    gap: var(--gap);
    font-size: 2rem;
    background: var(--card-background);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
}
.budget-card:hover {
    background: var(--card-hover);
}
.budget-card input {
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
}
.budget-card:has(input[type="radio"]:checked) {
    border: 3px solid var(--primary);
    background: var(--light);
}
.budget-card:has(input[type="radio"]:focus-visible) {
    outline: 5px solid var(--outline)
}

</style>