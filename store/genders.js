export const state = () => ({
  genders: [
    { name: 'Select your gender', value: '' },
    { name: 'Male', value: 'male' },
    { name: 'Female', value: 'female' },
    { name: 'Prefer not to say', value: 'prefer-not-to-say' },
  ],
});

export const getters = {
  genders(state) {
    return state.genders;
  },
};
