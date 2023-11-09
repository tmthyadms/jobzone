<template>
  <div>
    <HeroHome />
    <AppModal
      v-if="profile.accType === 'business'"
      title="Create job posting"
      modal-id="modal-job-post"
    >
      <form id="form-job-post" class="app-form" @submit.prevent="createJobPost">
        <AppInput
          label="job title"
          prompt="Enter the job title"
          input-id="title"
          :req="true"
          ac="organization-title"
          @input="(value) => (form.title = value)"
        />
        <AppInput
          label="department"
          prompt="Enter the department"
          input-id="department"
          :req="true"
          @input="(value) => (form.department = value)"
        />
        <InputSelect
          label="location"
          select-id="location"
          :req="true"
          ac="country-name"
          :options="countries"
          @change="(value) => (form.location = value)"
        />
        <InputSelect
          label="employment type"
          select-id="employmentType"
          :req="true"
          :options="employmentType"
          @change="(value) => (form.employmentType = value)"
        />
        <div class="app-flex-row">
          <AppInput
            label="min. salary range"
            type="number"
            prompt="Enter an amount"
            input-id="min-salary"
            class="flex-1"
            @input="(value) => (form.salaryRange.min = value)"
          />
          <AppInput
            label="max. salary range"
            type="number"
            prompt="Enter an amount"
            input-id="max-salary"
            class="flex-1"
            @input="(value) => (form.salaryRange.max = value)"
          />
        </div>
        <InputSelect
          label="required experience"
          select-id="requiredExp"
          :req="true"
          :options="requiredExp"
          @change="(value) => (form.requiredExp = value)"
        />
        <InputSelect
          label="required education"
          select-id="requiredEdu"
          :req="true"
          :options="requiredEdu"
          @change="(value) => (form.requiredEdu = value)"
        />
        <InputSelect
          label="industry"
          select-id="industry"
          :req="true"
          :options="industries"
          @change="(value) => (form.industry = value)"
        />
        <InputSelect
          label="functions"
          select-id="functions"
          :req="true"
          :options="functions"
          @change="(value) => (form.function = value)"
        />
        <InputTextarea
          label="job description"
          prompt="Enter the job description"
          text-area-id="desc"
          :req="true"
          @input="(value) => (form.desc = value)"
        />
        <AppInput
          label="requirements"
          prompt="Enter the requirements"
          input-id="requirements"
          :req="true"
          @input="(value) => (form.requirements = value)"
        />
        <AppInput
          label="benefits"
          prompt="Enter the benefits"
          input-id="benefits"
          :req="true"
          @input="(value) => (form.benefits = value)"
        />
        <button
          type="submit"
          class="btn btn-primary"
          :disabled="isFormSubmitted"
        >
          <span v-if="isFormSubmitted" class="loading loading-infinity"></span>
          <span v-else>create</span>
        </button>
      </form>
    </AppModal>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import employmentType from '@/assets/data/job-posting/employment-type.json';
import requiredExp from '@/assets/data/job-posting/required-exp.json';
import requiredEdu from '@/assets/data/job-posting/required-edu.json';
import industries from '@/assets/data/job-posting/industries.json';
import functions from '@/assets/data/job-posting/functions.json';

export default {
  data() {
    return {
      employmentType,
      requiredExp,
      requiredEdu,
      industries,
      functions,
      form: {
        title: '',
        department: '',
        location: '',
        employmentType: '',
        salaryRange: {
          min: '',
          max: '',
        },
        requiredExp: '',
        requiredEdu: '',
        industry: '',
        function: '',
        desc: '',
        requirements: '',
        benefits: '',
      },
      isFormSubmitted: false,
    };
  },
  computed: {
    ...mapGetters('countries', ['countries']),
    ...mapGetters('profile', ['profile']),
  },
  methods: {
    ...mapActions('job-posts', ['fetchJobPosts']),
    ...mapActions('countries', ['fetchCountries']),
    async createJobPost() {
      const formJobPost = document.getElementById('form-job-post');
      const modalJobPost = document.getElementById('modal-job-post');
      console.log(this.form);
      const formData = { ...{ bizId: this.profile.id }, ...this.form };
      this.isFormSubmitted = true;
      await this.$axios.$post('/createJobPosting', formData, {
        headers: { 'Content-Type': 'application/json' },
      });
      this.isFormSubmitted = false;
      formJobPost.reset();
      modalJobPost.classList.remove('modal-open');
      this.fetchJobPosts();
    },
  },
  async fetch() {
    await this.fetchCountries();
  },
};
</script>
