export const state = () => ({
  recent: {
    exp: {
      jobTitle: '',
      company: '',
    },
    edu: {
      levelEdu: '',
      fieldStudy: '',
    },
  },
});

export const getters = {
  recentExp: (state) => state.recent.exp,
  recentEdu: (state) => state.recent.edu,
};

export const mutations = {
  setRecentExp(state, payload) {
    state.recent.exp = payload;
  },
  setRecentEdu(state, payload) {
    state.recent.edu = payload;
  },
};

export const actions = {
  setRecentExp({ commit }, payload) {
    commit('setRecentExp', payload);
  },
  setRecentEdu({ commit }, payload) {
    commit('setRecentEdu', payload);
  },
  clearRecentExp({ commit }) {
    commit('setRecentExp', {
      jobTitle: '',
      company: '',
    });
  },
  clearRecentEdu({ commit }) {
    commit('setRecentEdu', {
      levelEdu: '',
      fieldStudy: '',
    });
  },
};
