<template>
    <div class="budget-select">
        <div class="cards">
            <BudgetCard icon="£" label="Low" type="low" :min="low.min" :max="low.max" @select="updateSelectedRange" :selected="selectedMin === low.min && selectedMax === low.max" />
            <BudgetCard icon="££" label="Mid" type="mid" :min="mid.min" :max="mid.max" @select="updateSelectedRange" :selected="selectedMin === mid.min && selectedMax === mid.max" />
            <BudgetCard icon="£££" label="High" type="high" :min="high.min" :max="high.max" @select="updateSelectedRange" :selected="selectedMin === high.min && selectedMax === high.max" />
        </div>

        <span class="help-text"> Drag the sliders to set your own range </span>

        <RangeSlider 
            @updateRange="updateSelectedRange"
            :min="low.min"
            :max="high.max"            :modelMin="selectedMin"
            :modelMax="selectedMax"
        />

    </div>
</template>

<script>
    import BudgetCard from '../elements/BudgetCard.vue'
    import RangeSlider from '../elements/RangeSlider.vue'

    export default {
        name: "BudgetSelect",
        props: {
            low: {
                type: Object,
                default: () => ({
                    "min": 0,
                    "max": 100,
                }),
            },
            mid: {
                type: Object,
                default: () => ({
                    "min": 100,
                    "max": 500,
                }),
            },
            high: {
                type: Object,
                default: () => ({
                    "min": 500,
                    "max": 750,
                }),
            },
        },
        components: {
            BudgetCard,
            RangeSlider,
        },
        data() {
            return {
                selectedMin: 0,
                selectedMax: 10,
            };
        },
        methods: {
            updateSelectedRange(event) {
                this.selectedMin = event.min;
                this.selectedMax = event.max;
                this.$emit("budgetUpdate", {
                    min: this.selectedMin,
                    max: this.selectedMax,
                });
            }
        },
    }
</script>

<style scoped>
.budget-select {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: var(--gap);
}
.cards {
    display: flex;
    gap: 20px;
    width: 100%;
    height: 100%;
    margin-bottom: 2rem;
}
</style>