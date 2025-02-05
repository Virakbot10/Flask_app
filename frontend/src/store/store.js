import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      authenticated: false,
      username: '',
      email: ''
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    clearUser(state) {
      state.user = {
        authenticated: false,
        username: '',
        email: ''
      }
    }
  }
})