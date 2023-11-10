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
  async deleteJobPost({ commit }, payload) {
    try {
      const data = await this.$axios.$post(
        `/deleteJobPosting`,
        { jobPostingId: payload },
        { headers: { 'Content-Type': 'application/json' } }
      );
      commit('setJobPosts', data);
    } catch (error) {
      console.error(error);
    }
  },
};
