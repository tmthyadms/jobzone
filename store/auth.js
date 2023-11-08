export const state = () => ({
  hasSignedIn: false,
});

export const getters = {
  hasSignedIn: (state) => state.hasSignedIn,
};

export const mutations = {
  setHasSignedIn(state, hasSignedIn) {
    state.hasSignedIn = hasSignedIn;
  },
};
