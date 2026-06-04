<template>
    <div class="budget-select">
        <div class="cards">
            <BudgetCard icon="£" label="Low" type="low" :min="low.min" :max="low.max" @select="updateSelectedRange" :selected="selectedMin === low.min && selectedMax === low.max" />
            <BudgetCard icon="££" label="Mid" type="mid" :min="mid.min" :max="mid.max" @select="updateSelectedRange" :selected="selectedMin === mid.min && selectedMax === mid.max" />
            <BudgetCard icon="£££" label="High" type="high" :min="high.min" :max="high.max" @select="updateSelectedRange" :selected="selectedMin === high.min && selectedMax === high.max" />
        </div>

        <div class="range-help">
            <AppButton 
                text="Set to min"
                :disabled="selectedMin === low.min"
                @click="resetFloor"
            />
            <span class="help-text"> Drag the sliders to set your own range </span>
            <AppButton 
                text="Set to max"
                :disabled="selectedMax === high.max"
                @click="resetCeil"
            />
        </div>

        <RangeSlider 
            @updateRange="updateSelectedRange"
            :min="low.min"
            :max="high.max"            
            :modelMin="selectedMin"
            :modelMax="selectedMax"
        />

    </div>
</template>

<script>
    import AppButton from '@/elements/AppButton.vue';
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
            selectedMin: {
                type: Number,
                default: 0,
            },
            selectedMax: {
                type: Number,
                default: 10,
            },
        },
        components: {
            BudgetCard,
            AppButton,
            RangeSlider,
        },
        methods: {
            updateSelectedRange(event) {
                this.$emit("budgetUpdate", {
                    min: event.min,
                    max: event.max,
                });
            },
            resetFloor() {
                this.$emit("resetFloor");
            },
            resetCeil() {
                this.$emit("resetCeil");
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
.range-help {
    justify-content: space-between;
    align-items: center;
    display: flex;
    width: 100%;
}
</style>