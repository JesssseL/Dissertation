<template>
    <div class="selectable_image_element">
        <input
            :value="image" 
            type="checkbox" 
            :checked="checked" 
            @change="emitChange"
        />
        <label class="material-symbols-outlined">check</label>
        <img :src="image" />
    </div>
</template>

<script>
export default {
  props: {
    image: String,
    productPageToken: String,
    checked: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    emitChange() {
        this.$emit("selectImage", {
            productPageToken: this.productPageToken,
            checked: event.target.checked,
        });
    }
  }
}
</script>

<style>
.selectable_image_element {
    padding: 3px;
    position: relative;
    width: 100%;
    aspect-ratio: 1 / 1;
    overflow: hidden;
    border-radius: var(--border-radius);
    height: 100%;
}

.selectable_image_element img {
    object-fit: cover;
    width: 100%;
    height: 100%;
    border-radius: var(--border-radius);
}

.selectable_image_element label {
    position: absolute;
    right: 10px;
    top: 10px;
    background: var(--primary);
    padding: 5px;
    border-radius: 100%;
    height: 25px;
    width: 25px;
    align-items: center;
    justify-content: center;
    display: flex;
    color: white;
    opacity: 0;
}

.selectable_image_element:has(input[type="checkbox"]:checked) {
    background-color: var(--primary);
}
.selectable_image_element:has(input[type="checkbox"]:checked) label {
    opacity: 1;
}
.selectable_image_element:has(input[type="checkbox"]:focus-visible img) {
    outline: 5px solid var(--outline);
    outline-offset: 3px;
}

.selectable_image_element input{
    width: 100%;
    height: 100%;
    opacity: 0;
    top: 0px;
    left: 0px;
    position: absolute;
    cursor: pointer;
}
</style>