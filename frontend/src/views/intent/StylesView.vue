<template>
    <div class="style container">
        <div class="header">
          <h1> Pick styles you like </h1>
          <h2> Subheading Subheading </h2>
        </div>

        <div class="style_options">
            <SelectableImage 
              v-for="photo in photos"
              :image="photo.image"
              :productPageToken="photo.productPageToken"
              :checked="photo.checked"
              @selectImage="imageChanged"
            />
        </div>

        <AppButton 
          text="Next"
          :disabled="selectedPhotos.length === 0"
          rightIcon="arrow_forward"
          @click="saveSelected"
        />
    </div>
</template>

<script>
import AppButton from '@/elements/AppButton.vue'
import SelectableImage from '@/elements/SelectableImage.vue'
import { useSearchStore } from '../../stores/searchStore'
import { useDiscoveryStore } from '../../stores/discoveryStore'

export default {
  name: "StylesView",
  components: {
    AppButton,
    SelectableImage
  },
  data() {
    return {
      searchStore: useSearchStore(),
      discoveryStore: useDiscoveryStore(),
      photos: [],
    }
  },
  computed: {
    selectedPhotos() {
      return this.photos.filter(p => p.checked)
    }
  },
  mounted() {
    this.photos = this.discoveryStore.photos.map(photo => ({
      name: photo.name,
      image: photo.image,
      productPageToken: photo.productPageToken,
      checked: false
    }))
    console.log(this.photos)
  },
  methods: {
    imageChanged(event) {
      const photo = this.photos.find(
        p => p.productPageToken === event.productPageToken
      )
      if (photo) {
        photo.checked = event.checked
      }
      console.log(this.selectedPhotos)
    },
    saveSelected() {
      this.searchStore.addPhotos(this.selectedPhotos)
      this.$router.push('/budget')
    },
  },
};
</script>

<style scoped>
.style {
  display: flex;
  flex-direction: column;
  height: 100%;
  gap: var(--gap);
  overflow: hidden;
}
.style_options {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--gap);
  width: 100%;
  height: 80%;
}
button {
  margin-top: auto;
  align-self: flex-end;
}
</style>