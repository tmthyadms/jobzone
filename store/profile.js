export const state = () => ({
  common: {
    id: '',
    accType: '',
    email: '',
    placeholder: '',
    fullName: '',
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
  setFullName(state, payload) {
    state.common.fullName = payload;
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
  setProfile(state) {
    const accType = state.common.accType;
    const accTypeDetails =
      accType === 'job-seeker' ? { ...state.jobSeeker } : { ...state.business };
    state.profile = { ...state.common, ...accTypeDetails };
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
      commit('setProfile');
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
      commit('setProfile');
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
    commit('setProfile');
  },
  async fetchProfile({ dispatch, commit, state }, payload) {
    try {
      await dispatch('fetchAuth', payload);
      const accType = state.common.accType;
      if (accType === 'job-seeker') {
        await dispatch('fetchJobSeeker', payload);
        const name = state.jobSeeker.name;
        const fullName = `${name.first} ${name.last}`;
        let placeholder = `${name.first[0]}${name.last[0]}`;
        placeholder = placeholder.toUpperCase();
        commit('setFullName', fullName);
        commit('setPlaceholder', placeholder);
      } else if (accType === 'business') {
        await dispatch('fetchBusiness', payload);
        const fullName = state.business.bizName;
        let placeholder = state.business.bizName[0];
        placeholder = placeholder.toUpperCase();
        commit('setFullName', fullName);
        commit('setPlaceholder', placeholder);
      }
      await commit('setProfile'); // for setting placeholder
    } catch (error) {
      console.error(error);
    }
  },
  async updateAuth({ dispatch }, payload) {
    try {
      let auth = { authId: payload.authId };
      if (payload.email) auth.email = payload.email;
      await this.$axios.$post('/updateAuth', auth, {
        headers: { 'Content-Type': 'application/json' },
      });
      await dispatch('fetchAuth', payload.authId);
    } catch (error) {
      console.error(error);
    }
  },
  async updateJobSeeker({ dispatch }, payload) {
    try {
      let jobSeeker = { jobSeekerId: payload.jobSeekerId };
      if (payload.name?.first) {
        jobSeeker.name = {
          first: payload.name.first,
          last: payload.name.last,
        };
      }
      if (payload.gender) jobSeeker.gender = payload.gender;
      if (payload.country) jobSeeker.country = payload.country;
      if (payload.recentExp?.jobTitle) {
        jobSeeker.recentExp = {
          jobTitle: payload.recentExp.jobTitle,
          company: payload.recentExp.company,
        };
      } else {
        jobSeeker.recentExp = {
          jobTitle: '',
          company: '',
        };
      }
      if (payload.recentEdu?.levelEdu) {
        jobSeeker.recentEdu = {
          levelEdu: payload.recentEdu.levelEdu,
          fieldStudy: payload.recentEdu.fieldStudy,
        };
      } else {
        jobSeeker.recentEdu = {
          levelEdu: '',
          fieldStudy: '',
        };
      }
      await this.$axios.$post('/updateJobSeeker', jobSeeker, {
        headers: { 'Content-Type': 'application/json' },
      });
      await dispatch('fetchJobSeeker', payload.jobSeekerId);
    } catch (error) {
      console.error(error);
    }
  },
  async updateBusiness({ dispatch }, payload) {
    try {
      let business = { bizId: payload.bizId };
      if (payload.bizName) business.bizName = payload.bizName;
      if (payload.bizProfile) business.bizProfile = payload.bizProfile;
      if (payload.regNum) business.regNum = payload.regNum;
      if (payload.address) business.address = payload.address;
      if (payload.bizSize) business.bizSize = payload.bizSize;
      await this.$axios.$post('/updateBusiness', business, {
        headers: { 'Content-Type': 'application/json' },
      });
      await dispatch('fetchBusiness', payload.bizId);
    } catch (error) {
      console.error(error);
    }
  },
};
