<template>
  <div>
    <HeroSignUp />
    <AppModal title="Add work experience" modal-id="modal-exp">
      <form id="form-exp" class="app-form" @submit.prevent="addExp">
        <AppInput label="job title" input-id="job-title" :req="true" />
        <AppInput label="company" input-id="company" :req="true" />
        <button type="submit" class="btn btn-primary">add</button>
      </form>
    </AppModal>
    <AppModal title="Add education" modal-id="modal-edu">
      <form id="form-edu" class="app-form" @submit.prevent="addEdu">
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
      const modalEdu = document.getElementById('modal-exp');
      const formExp = document.getElementById('form-exp');
      const jobTitle = document.getElementById('job-title').value;
      const company = document.getElementById('company').value;
      this.setRecentExp({ jobTitle, company });
      formExp.reset();
      modalEdu.classList.remove('modal-open');
    },
    addEdu() {
      const modalExp = document.getElementById('modal-edu');
      const formEdu = document.getElementById('form-edu');
      const levelEdu = document.getElementById('level-edu').value;
      const fieldStudy = document.getElementById('field-study').value;
      this.setRecentEdu({ levelEdu, fieldStudy });
      formEdu.reset();
      modalExp.classList.remove('modal-open');
    },
  },
};
</script>
