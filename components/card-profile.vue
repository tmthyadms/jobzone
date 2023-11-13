<template>
  <AppCard class="bg-base-200 app-shadow-b">
    <template #body>
      <form
        id="form-update-profile"
        class="grid grid-cols-1 gap-6"
        @submit.prevent="updateProfile"
      >
        <h2
          class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
        >
          Customize profile
        </h2>
        <template v-if="profile.accType === 'job-seeker'">
          <AppInput
            label="first name"
            :prompt="profile.name.first"
            input-id="first-name"
            :disabled="!isEditing"
            ac="given-name"
            @input="(value) => (form.jobSeeker.name.first = value)"
          />
          <AppInput
            label="last name"
            :prompt="profile.name.last"
            input-id="last-name"
            :disabled="!isEditing"
            ac="family-name"
            @input="(value) => (form.jobSeeker.name.last = value)"
          />
          <InputSelect
            label="gender"
            select-id="gender"
            :disabled="!isEditing"
            ac="sex"
            :options="genders"
            :value="profile.gender"
            @change="(value) => (form.jobSeeker.gender = value)"
          />
          <InputSelect
            label="country"
            select-id="country"
            :disabled="!isEditing"
            ac="country-name"
            :options="countries"
            :value="profile.country"
            @change="(value) => (form.jobSeeker.country = value)"
          />
          <AppInputModal
            label="most recent work experience"
            tip="Click to add work experience"
            modal-id="modal-exp"
            :disabled="!isEditing"
          />
          <CardRecent
            v-if="recentExp?.jobTitle"
            :title="recentExp.jobTitle"
            :subtitle="recentExp.company"
            :disabled="!isEditing"
            @clear="clearRecentExp"
            class="bg-base-200"
          />
          <AppInputModal
            label="most recent education"
            tip="Click to add education"
            modal-id="modal-edu"
            :disabled="!isEditing"
          />
          <CardRecent
            v-if="recentEdu?.levelEdu"
            :title="recentEdu.levelEdu"
            :subtitle="recentEdu.fieldStudy"
            :disabled="!isEditing"
            @clear="clearRecentEdu"
            class="bg-base-200"
          />
        </template>
        <template v-if="profile.accType === 'business'">
          <AppInput
            label="business name"
            :prompt="profile.bizName"
            input-id="biz-name"
            :disabled="!isEditing"
            ac="organization"
            @input="(value) => (form.business.bizName = value)"
          />
          <InputTextarea
            label="business profile"
            :prompt="profile.bizProfile"
            text-area-id="biz-profile"
            :disabled="!isEditing"
            @input="(value) => (form.business.bizProfile = value)"
          />
          <AppInput
            label="registration number"
            :prompt="profile.regNum"
            input-id="reg-num"
            :disabled="!isEditing"
            @input="(value) => (form.business.regNum = value)"
          />
          <AppInput
            label="address"
            :prompt="profile.address"
            input-id="address"
            :disabled="!isEditing"
            ac="street-address"
            @input="(value) => (form.business.address = value)"
          />
          <InputSelect
            label="business size"
            select-id="biz-size"
            :disabled="!isEditing"
            :options="bizSize"
            :value="profile.bizSize"
            @change="(value) => (form.business.bizSize = value)"
          />
        </template>
        <div class="space-y-2">
          <button
            type="button"
            class="btn btn-block btn-primary"
            :class="{ 'btn-outline': isEditing && !isFormSubmitted }"
            :disabled="isFormSubmitted"
            @click="isEditing = !isEditing"
          >
            {{ isEditing ? 'cancel editing' : 'edit profile' }}
          </button>
          <button
            v-if="isEditing"
            type="submit"
            name="sign-up"
            class="btn btn-block btn-primary"
            :disabled="isFormSubmitted"
          >
            <span
              v-if="isFormSubmitted"
              class="loading loading-infinity"
            ></span>
            <span v-else>update profile</span>
          </button>
        </div>
      </form>
    </template>
  </AppCard>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';
import genders from '@/assets/data/job-seeker/genders.json';
import bizSize from '@/assets/data/business/biz-size.json';

export default {
  data() {
    return {
      genders,
      bizSize,
      form: {
        jobSeeker: {
          jobSeekerId: '',
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
          bizId: '',
          bizName: '',
          bizProfile: '',
          regNum: '',
          address: '',
          bizSize: '',
        },
      },
      isFormSubmitted: false,
      isEditing: false,
    };
  },
  computed: {
    ...mapGetters('profile', ['profile']),
    ...mapGetters('countries', ['countries']),
    ...mapGetters('qualifications', ['recentExp', 'recentEdu']),
  },
  watch: {
    recentExp(newValue) {
      this.form.jobSeeker.recentExp = {
        jobTitle: newValue.jobTitle,
        company: newValue.company,
      };
    },
    recentEdu(newValue) {
      this.form.jobSeeker.recentEdu = {
        levelEdu: newValue.levelEdu,
        fieldStudy: newValue.fieldStudy,
      };
    },
    isEditing(newValue) {
      // reset form when editing is cancelled
      // due to not using v-model, we need to reset the form manually
      if (!newValue) {
        document.getElementById('form-update-profile').reset();
        if (this.profile.accType === 'job-seeker') {
          this.form.jobSeeker.name = {
            first: '',
            last: '',
          };
          this.form.jobSeeker.gender = '';
          this.form.jobSeeker.country = '';
          this.form.jobSeeker.recentExp = {
            jobTitle: '',
            company: '',
          };
          this.form.jobSeeker.recentEdu = {
            levelEdu: '',
            fieldStudy: '',
          };
        } else if (this.profile.accType === 'business') {
          this.form.business.bizName = '';
          this.form.business.bizProfile = '';
          this.form.business.regNum = '';
          this.form.business.address = '';
          this.form.business.bizSize = '';
        }
      }
      // reset recentExp and recentEdu when editing is cancelled
      if (this.profile.accType === 'job-seeker') {
        const hasRecentExp =
          this.recentExp?.jobTitle === this.profile?.recentExp?.jobTitle;
        const hasRecentEdu =
          this.recentEdu?.levelEdu === this.profile?.recentEdu?.levelEdu;
        if (!newValue) {
          if (!hasRecentExp) this.setRecentExp(this.profile.recentExp);
          if (!hasRecentEdu) this.setRecentEdu(this.profile.recentEdu);
        }
      }
    },
  },
  created() {
    if (this.profile.accType === 'job-seeker') {
      this.setRecentExp(this.profile.recentExp);
      this.setRecentEdu(this.profile.recentEdu);
    }
  },
  methods: {
    ...mapMutations('qualifications', [
      'setRecentExp',
      'setRecentEdu',
      'clearRecentExp',
      'clearRecentEdu',
    ]),
    ...mapActions('countries', ['fetchCountries']),
    ...mapActions('profile', ['updateJobSeeker', 'updateBusiness']),
    async updateProfile() {
      try {
        this.isFormSubmitted = true;
        if (this.profile.accType === 'job-seeker') {
          this.form.jobSeeker.jobSeekerId = this.profile.id;
          await this.updateJobSeeker(this.form.jobSeeker);
        } else if (this.profile.accType === 'business') {
          this.form.business.bizId = this.profile.id;
          await this.updateBusiness(this.form.business);
        }
        this.isFormSubmitted = false;
        this.isEditing = false;
        this.$toast.success('Profile updated successfully.');
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
