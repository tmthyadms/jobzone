export const state = () => ({
  accType: [
    { name: 'Select your account type', value: '' },
    { name: 'Job seeker', value: 'job-seeker' },
    { name: 'Business', value: 'business' },
  ],
});

export const getters = {
  accType: (state) => state.accType,
};
