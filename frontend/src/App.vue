<template>
  <BurgerMenu 
    :currentRoute="$route.name" />
  <router-view />
  <AiPannel 
    :currentRoute="$route.name" />
</template>

<script>
import BurgerMenu from '@/components/BurgerMenu.vue'
import AiPannel from '@/components/AiPannel.vue'

export default {
  name: "App",
  components: {
    BurgerMenu,
    AiPannel
  },
};
</script>