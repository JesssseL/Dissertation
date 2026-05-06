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
            <h3> {{label}} </h3>
            <p> {{getBudgetText()}} </p>
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

                    case 'mid':
                        return `Over £${this.min}`

                    case 'high':
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
  font-size: 2rem;
}
</style>