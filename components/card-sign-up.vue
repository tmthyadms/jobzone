<template>
  <AppCard>
    <template #body>
      <AppComboMark class="justify-center lg:justify-start mb-6" />
      <h2
        class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
      >
        Join us to find <br class="hidden lg:inline" />
        your dream job
      </h2>
      <form class="grid grid-cols-1 gap-6" @submit.prevent="signUp">
        <InputSelect
          label="account type"
          select-id="acc-type"
          :req="true"
          :options="accType"
          @change="(value) => (form.auth.accType = value)"
        />
        <AppInput
          label="email"
          type="email"
          input-id="email"
          :req="true"
          ac="email"
          @input="(value) => (form.auth.email = value)"
        />
        <InputPassword @input="(value) => (form.auth.password = value)" />
        <template v-if="form.auth.accType === 'job-seeker'">
          <AppInput
            label="first name"
            input-id="first-name"
            :req="true"
            ac="given-name"
            @input="(value) => (form.jobSeeker.name.first = value)"
          />
          <AppInput
            label="last name"
            input-id="last-name"
            :req="true"
            ac="family-name"
            @input="(value) => (form.jobSeeker.name.last = value)"
          />
          <InputSelect
            label="gender"
            select-id="gender"
            ac="sex"
            :options="genders"
            @change="(value) => (form.jobSeeker.gender = value)"
          />
          <InputSelect
            label="country"
            select-id="country"
            :req="true"
            ac="country-name"
            :options="countries"
            @change="(value) => (form.jobSeeker.country = value)"
          />
          <AppInputModal
            label="most recent work experience"
            tip="Click to add work experience"
            modal-id="modal-exp"
          />
          <CardRecent
            v-if="recentExp?.jobTitle"
            :title="recentExp.jobTitle"
            :subtitle="recentExp.company"
            @clear="clearRecentExp"
          />
          <AppInputModal
            label="most recent education"
            tip="Click to add education"
            modal-id="modal-edu"
          />
          <CardRecent
            v-if="recentEdu?.levelEdu"
            :title="recentEdu.levelEdu"
            :subtitle="recentEdu.fieldStudy"
            @clear="clearRecentEdu"
          />
        </template>
        <template v-if="form.auth.accType === 'business'">
          <AppInput
            label="business name"
            input-id="biz-name"
            :req="true"
            ac="organization"
            @input="(value) => (form.business.bizName = value)"
          />
          <InputTextarea
            label="business profile"
            text-area-id="biz-profile"
            :req="true"
            @input="(value) => (form.business.bizProfile = value)"
          />
          <AppInput
            label="registration number"
            input-id="reg-num"
            :req="true"
            @input="(value) => (form.business.regNum = value)"
          />
          <AppInput
            label="address"
            input-id="address"
            :req="true"
            ac="street-address"
            @input="(value) => (form.business.address = value)"
          />
          <InputSelect
            label="business size"
            select-id="biz-size"
            :req="true"
            :options="bizSize"
            @change="(value) => (form.business.bizSize = value)"
          />
        </template>
        <button
          type="submit"
          name="sign-up"
          class="btn btn-block btn-primary"
          :disabled="isFormSubmitted"
        >
          <span v-if="isFormSubmitted" class="loading loading-infinity"></span>
          <span v-else>sign up</span>
        </button>
      </form>
      <NuxtLink
        to="/"
        class="btn btn-outline btn-primary"
        @click="$emit('flip')"
      >
        already on jobzone? sign in</NuxtLink
      >
    </template>
  </AppCard>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';
import accType from '@/assets/data/auth/acc-type.json';
import genders from '@/assets/data/job-seeker/genders.json';
import bizSize from '@/assets/data/business/biz-size.json';

export default {
  events: ['flip'],
  data() {
    return {
      accType,
      genders,
      bizSize,
      form: {
        auth: {
          accType: '',
          email: '',
          password: '',
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
      },
      isFormSubmitted: false,
    };
  },
  computed: {
    ...mapGetters('countries', ['countries']),
    ...mapGetters('qualifications', ['recentExp', 'recentEdu']),
  },
  watch: {
    recentExp(newValue) {
      this.form.jobSeeker.recentExp = newValue;
    },
    recentEdu(newValue) {
      this.form.jobSeeker.recentEdu = newValue;
    },
  },
  created() {
    this.clearRecentExp();
    this.clearRecentEdu();
  },
  methods: {
    ...mapMutations('qualifications', ['clearRecentExp', 'clearRecentEdu']),
    ...mapActions('countries', ['fetchCountries']),
    async signUp() {
      try {
        let formData = this.form.auth;
        if (this.form.auth.accType === 'job-seeker')
          formData = { ...formData, ...this.form.jobSeeker };
        else if (this.form.auth.accType === 'business')
          formData = { ...formData, ...this.form.business };
        this.isFormSubmitted = true;
        await this.$axios.$post('/createAuth', formData, {
          headers: { 'Content-Type': 'application/json' },
        });
        window.scrollTo({ top: 0, behavior: 'auto' });
        this.$toast.success('Account created successfully.');
        this.isFormSubmitted = false;
        this.$router.push('/');
      } catch (error) {
        this.isFormSubmitted = false;
        this.$toast.error(error.message);
      }
    },
  },
  async fetch() {
    await this.fetchCountries();
  },
};
</script>
