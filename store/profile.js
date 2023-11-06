export const state = () => ({
  common: {
    id: '',
    accType: '',
    email: '',
    placeholder: '',
  },
  jobSeeker: {
    name: {
      first: '',
      last: '',
    },
    gender: '',
    country: '',
    recentExp: {
      jobTitle: '',
      company: '',
    },
    recentEdu: {
      levelEdu: '',
      fieldStudy: '',
    },
  },
  business: {
    bizName: '',
    bizProfile: '',
    regNum: '',
    address: '',
    bizSize: '',
  },
  profile: {},
});

export const getters = {
  common: (state) => state.common,
  jobSeeker: (state) => state.jobSeeker,
  business: (state) => state.business,
  profile: (state) => state.profile,
};

export const mutations = {
  setCommon(state, payload) {
    state.common.id = payload._id;
    state.common.accType = payload.accountType;
    state.common.email = payload.email;
  },
  setPlaceholder(state, payload) {
    state.common.placeholder = payload;
  },
  setJobSeeker(state, payload) {
    state.jobSeeker = {
      name: {
        first: payload.name.first,
        last: payload.name.last,
      },
      gender: payload.gender,
      country: payload.country,
      recentExp: {
        jobTitle: payload.recentExperience.jobTitle,
        company: payload.recentExperience.company,
      },
      recentEdu: {
        levelEdu: payload.recentEducation.levelEducation,
        fieldStudy: payload.recentEducation.fieldStudy,
      },
    };
  },
  setBusiness(state, payload) {
    state.business = {
      bizName: payload.businessName,
      bizProfile: payload.businessProfile,
      regNum: payload.registrationNumber,
      address: payload.address,
      bizSize: payload.businessSize,
    };
  },
  setProfile(state, payload) {
    state.profile = { ...state.common, ...payload };
  },
};

export const actions = {
  async fetchAuth({ commit }, payload) {
    try {
      const dataAuth = await this.$axios.$post(
        '/auth',
        { authId: payload },
        { headers: { 'Content-Type': 'application/json' } }
      );
      commit('setCommon', dataAuth);
    } catch (error) {
      console.error(error);
    }
  },
  async fetchJobSeeker({ commit }, payload) {
    try {
      const dataJobSeeker = await this.$axios.$post(
        '/jobSeeker',
        { jobSeekerId: payload },
        { headers: { 'Content-Type': 'application/json' } }
      );
      commit('setJobSeeker', dataJobSeeker);
    } catch (error) {
      console.error(error);
    }
  },
  async fetchBusiness({ commit }, payload) {
    const dataBusiness = await this.$axios.$post(
      '/business',
      { bizId: payload },
      { headers: { 'Content-Type': 'application/json' } }
    );
    commit('setBusiness', dataBusiness);
  },
  async fetchProfile({ dispatch, commit, state }, payload) {
    try {
      await dispatch('fetchAuth', payload);
      const accType = state.common.accType;
      if (accType === 'job-seeker') {
        await dispatch('fetchJobSeeker', payload);
        const name = state.jobSeeker.name;
        let placeholder = `${name.first[0]}${name.last[0]}`;
        placeholder = placeholder.toUpperCase();
        commit('setPlaceholder', placeholder);
        commit('setProfile', state.jobSeeker);
      } else if (accType === 'business') {
        await dispatch('fetchBusiness', payload);
        let placeholder = state.business.bizName[0];
        placeholder = placeholder.toUpperCase();
        commit('setPlaceholder', placeholder);
        commit('setProfile', state.business);
      }
    } catch (error) {
      console.error(error);
    }
  },
};
