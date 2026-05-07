<template>
    <div class="selectable_tag_element">
        <input
            :value="label" 
            type="checkbox" 
            :checked="checked" 
            @change="emitChange"
        />
        <label>{{label}}</label>
    </div>
</template>

<script>
export default {
  props: {
    label: String,
    checked: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    emitChange() {
        console.log(event.target.checked)
        this.$emit("change", {
            label: this.label,
            checked: event.target.checked,
        });
    }
  }
}
</script>

<style scoped>
    .selectable_tag_element {
        display: flex;
        align-items: center;
        width: fit-content;
        position: relative;
        padding: var(--padding) calc(var(--padding) * 2);
        border-radius: var(--border-radius);
        border: 2px solid var(--border-secondary);
        color: var(--primary);
        margin: 0;
    }
    .tertiary {
        background-color: var(--card-background);
        border: 2px solid var(--primary);
        color: var(--primary);
    }
    .selectable_tag_element:hover {
        background: var(--card-hover);
    }

    .selectable_tag_element:has(input[type="checkbox"]:checked) {
        border: 2px solid var(--light);
        background: var(--light);
    }
    .selectable_tag_element:has(input[type="checkbox"]:checked):hover {
        border: 2px solid var(--light-hover);
        background: var(--light-hover);
    }
    .selectable_tag_element:has(input[type="checkbox"]:focus-visible) {
        outline: 1px solid black;
    }

    .selectable_tag_element input{
        width: 100%;
        height: 100%;
        opacity: 0;
        top: 0px;
        left: 0px;
        position: absolute;
        cursor: pointer;
    }
    .selectable_tag_element label {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        font-size: 0.8rem;
    }
    .selectable_tag_element label::before {
        font-family: 'Material Symbols Outlined';
        content: 'add';
        margin-right: 6px;
    }
    .selectable_tag_element:has(input[type="checkbox"]:checked) label::before {
        content: "check";
    }
</style>