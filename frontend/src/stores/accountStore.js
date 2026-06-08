import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useAccountStore = defineStore('account', () => {
  const email = ref('')
  const password = ref('')

  function setAccountDetails(newEmail, newPassword) {
    email.value = newEmail
    password.value = newPassword
  }

  const accountDetails = computed(() => ({
    email: email.value,
    password: password.value
  }))

  const isLoggedIn = computed(() =>
    email.value.length > 0 &&
    password.value.length > 0
  )

  function clearDetails() {
    email.value = ''
    password.value = ''
  }

  return {
    email,
    password,
    accountDetails,
    isLoggedIn,
    setAccountDetails,
    clearDetails
  }
})