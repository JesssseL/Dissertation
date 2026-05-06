<template>
    <div class="cards">
        <BudgetCard icon="£" label="Low" type="low" :min="low.min" :max="low.max" @select="updateSelectedRange" :selected="selectedRangeName === 'low'" />
        <BudgetCard icon="££" label="Mid" type="mid" :min="mid.min" :max="mid.max" @select="updateSelectedRange" :selected="selectedRangeName === 'mid'" />
        <BudgetCard icon="£££" label="High" type="high" :min="high.min" :max="high.max" @select="updateSelectedRange" :selected="selectedRangeName === 'high'" />
    </div>

    <RangeSlider 
        @updateRange="updateSelectedRange"
        :min="low.min"
        :max="high.max"
        :modelMin="selectedMin"
        :modelMax="selectedMax"
    />
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
                selectedMax: 100,
                selectedRangeName: null
            };
        },
        methods: {
            updateSelectedRange(event) {
                this.selectedMin = event.min;
                this.selectedMax = event.max;
                this.selectedRangeName = event.type;
            }
        },
    }
</script>

<style scoped>
</style>