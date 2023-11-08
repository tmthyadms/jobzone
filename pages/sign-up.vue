<template>
  <div>
    <HeroSignUp />
    <AppModal title="Add work experience" modal-id="exp_modal">
      <form
        action=""
        id="exp-form"
        class="grid grid-cols-1 gap-6"
        @submit.prevent="addExp"
      >
        <AppInput label="job title" input-id="job-title" :req="true" />
        <AppInput label="company" input-id="company" :req="true" />
        <button type="submit" class="btn btn-primary">add</button>
      </form>
    </AppModal>
    <AppModal title="Add education" modal-id="edu_modal">
      <form
        action=""
        id="edu-form"
        class="grid grid-cols-1 gap-6"
        @submit.prevent="addEdu"
      >
        <AppInput label="level of education" input-id="level-edu" :req="true" />
        <AppInput label="field of study" input-id="field-study" :req="true" />
        <button type="submit" class="btn btn-primary">add</button>
      </form>
    </AppModal>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  layout: 'pre-sign-in',
  methods: {
    ...mapActions('qualifications', ['setRecentExp', 'setRecentEdu']),
    addExp() {
      const eduModal = document.getElementById('exp_modal');
      const expForm = document.getElementById('exp-form');
      const jobTitle = document.getElementById('job-title').value;
      const company = document.getElementById('company').value;
      this.setRecentExp({ jobTitle, company });
      expForm.reset();
      eduModal.classList.remove('modal-open');
    },
    addEdu() {
      const expModal = document.getElementById('edu_modal');
      const eduForm = document.getElementById('edu-form');
      const levelEdu = document.getElementById('level-edu').value;
      const fieldStudy = document.getElementById('field-study').value;
      this.setRecentEdu({ levelEdu, fieldStudy });
      eduForm.reset();
      expModal.classList.remove('modal-open');
    },
  },
};
</script>
