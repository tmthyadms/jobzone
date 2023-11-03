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
  recentExp(state) {
    return state.recent.exp;
  },
  recentEdu(state) {
    return state.recent.edu;
  },
};

export const mutations = {
  setRecentExp(state, data) {
    state.recent.exp = data;
  },
  setRecentEdu(state, data) {
    state.recent.edu = data;
  },
};

export const actions = {
  setRecentExp({ commit }, data) {
    commit('setRecentExp', data);
  },
  setRecentEdu({ commit }, data) {
    commit('setRecentEdu', data);
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
