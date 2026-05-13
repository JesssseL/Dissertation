const API_BASE_URL = 'http://localhost:8000'

export async function apiRequest(endpoint, options = {}, mockResponse) {
  await new Promise(resolve => setTimeout(resolve, 3000)) //TODO - api call

  console.log('endpoint', `${API_BASE_URL}${endpoint}`)
  console.log('options', options)

  return mockResponse
}