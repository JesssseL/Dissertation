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
        padding: 5px 10px;
        border-radius: 5px;
        border: 0;
        margin: 0;
        background-color: lightgrey;
    }

    .selectable_tag_element:has(input[type="checkbox"]:checked) {
        background-color: var(--light-green); 
        color: var(--green);
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
        display: inline-flex
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