export const state = () => ({
  jobPosts: [],
});

export const getters = {
  jobPosts: (state) => state.jobPosts,
};

export const mutations = {
  setJobPosts(state, payload) {
    state.jobPosts = payload;
  },
};

export const actions = {
  async fetchJobPosts({ commit }) {
    try {
      const data = await this.$axios.$post('/jobPostings');
      commit('setJobPosts', data);
    } catch (error) {
      console.error(error);
    }
  },
};
