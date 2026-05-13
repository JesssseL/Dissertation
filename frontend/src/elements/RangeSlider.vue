<template>
    <div class="range-slider">
        <input 
            type=number 
            class="slider-input"
            v-model="minValue"
            :min="min"
            :max="max"
            @change="lowRangeChange"
        />
        <div class="slider-container">
            <div class="slider-track"></div>
            <div class="slider-range" :style="rangeStyle"></div>
            <input
                type="range"
                :min="min"
                :max="max"
                v-model.number="minValue"
                @input="lowRangeChange"
                class="thumb thumb-left"
            />
            <input
                type="range"
                :min="min"
                :max="max"
                v-model.number="maxValue"
                @input="highRangeChange"
                class="thumb thumb-right"
            />
        </div>
        <input 
            type=number
            class="slider-input"
            v-model="maxValue"
            :min="min"
            :max="max"
            @change="highRangeChange"
        />
    </div>
</template>

<script>
export default {
  name: "RangeSlider",
  props: {
    min: {
      type: Number,
      default: 0,
    },
    max: {
      type: Number,
      default: 100,
    },
    modelMin: Number,
    modelMax: Number,
  },
  data() {
    return {
      minValue: this.min,
      maxValue: this.max,
    };
  },
  watch: {
    modelMin(newVal) {
      this.minValue = newVal;
    },
    modelMax(newVal) {
      this.maxValue = newVal;
    }
  },
  computed: {
    rangeStyle() {
      const left =
        ((this.minValue - this.min) / (this.max - this.min)) * 100;
      const right =
        ((this.maxValue - this.min) / (this.max - this.min)) * 100;

      return {
        left: `${left}%`,
        width: `${right - left}%`,
      };
    },
  },
  methods: {
    lowRangeChange() {
      if (this.minValue > this.maxValue - 1) {
        this.minValue = this.maxValue - 1;
      }
      if (this.minValue < this.min) {
        this.minValue = this.min;
      }

      this.emitChange();
    },
    highRangeChange() {
      if (this.maxValue < this.minValue + 1) {
        this.maxValue = this.minValue + 1;
      }
      if (this.maxValue > this.max) {
        this.maxValue = this.max;
      }

      this.emitChange();
    },
    emitChange() {
      this.$emit("updateRange", {
        min: this.minValue,
        max: this.maxValue,
      });
    },
  },
};
</script>

<style scoped>
.range-slider {
    display: flex;
    gap: var(--gap);
    width: 100%;
    height: fit-content;
}
.slider-input {
    background: var(--secondary);
    text-align: center;
    border: 0;

    background: var(--card-background);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    padding: var(--padding);
    color: var(--primary)
}
.slider-container {
  position: relative;
  width: 100%;
  height: 40px; /* important for vertical centering */
  overflow: hidden;
}

.slider-track,
.slider-range {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  height: 6px;
  border-radius: 3px;
}

.slider-track {
  width: 100%;
  background: #ddd;
}

.slider-range {
  background: var(--primary);
}

input[type="range"] {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 100%;
  margin: 0;
  pointer-events: none;
  appearance: none;
  background: none;
}

input[type="range"]::-webkit-slider-thumb {
  pointer-events: all;
  appearance: none;

  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--primary);

  cursor: pointer;
  margin-top: 0; /* important fix for Chrome offset */
}

input[type="range"]::-moz-range-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--primary);
  cursor: pointer;
  border: none;
}

input[type="range"]:focus {
  outline: none;
}

input[type="range"]:focus-visible::-webkit-slider-thumb {
  width: 34px;
  height: 34px;

  background:
    radial-gradient(
      circle,
      var(--primary) 0 9px,
      var(--background) 9px 12px,
      var(--outline) 12px 17px
    );
}

input[type="range"]:focus-visible::-moz-range-thumb {
  width: 34px;
  height: 34px;

  background:
    radial-gradient(
      circle,
      var(--primary) 0 9px,
      var(--background) 9px 12px,
      var(--outline) 12px 17px
    );
}

/*
Source - https://stackoverflow.com/a/23715905
Posted by rink.attendant.6
Retrieved 2026-05-06, License - CC BY-SA 3.0
*/

input[type='number']::-webkit-inner-spin-button, 
input[type='number']::-webkit-outer-spin-button { 
    -webkit-appearance: none;
    margin: 0;
}
</style>