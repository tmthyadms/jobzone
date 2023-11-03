export const state = () => ({
  countries: [{ name: 'Select your country', value: '' }],
});

export const getters = {
  countries(state) {
    return state.countries;
  },
};

export const mutations = {
  setCountries(state, countries) {
    let newCountries = countries
      .map((country) => {
        return {
          name: country.name.common,
          value: country.name.common,
        };
      })
      .filter((country) => country.name !== 'Israel');
    newCountries.sort((a, b) => a.name.localeCompare(b.name));
    newCountries.unshift({ name: 'Select your country' });
    state.countries = newCountries;
  },
};

export const actions = {
  async fetchCountries({ commit }) {
    try {
      const data = await this.$axios.$get('https://restcountries.com/v3.1/all');
      commit('setCountries', data);
    } catch (error) {
      console.log(error);
    }
  },
};
