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
    state.recent.exp = {
      jobTitle: payload.jobTitle,
      company: payload.company,
    };
  },
  setRecentEdu(state, payload) {
    state.recent.edu = {
      levelEdu: payload.levelEdu,
      fieldStudy: payload.fieldStudy,
    };
  },
  clearRecentExp(state) {
    state.recent.exp = {
      jobTitle: '',
      company: '',
    };
  },
  clearRecentEdu(state) {
    state.recent.edu = {
      levelEdu: '',
      fieldStudy: '',
    };
  },
};
