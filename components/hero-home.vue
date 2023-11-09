<template>
  <div class="min-h-screen">
    <AppHero :fit="true">
      <div
        class="flex flex-col lg:flex-row items-center justify-between gap-2 lg:gap-0"
      >
        <InputSearch
          prompt="Enter keywords, company, or job title"
          search-id="search-job"
          class="w-72 lg:w-96"
        />
        <div class="flex justify-center gap-2">
          <div class="tooltip tooltip-left" data-tip="Refresh job posts">
            <button class="btn btn-ghost" @click="fetchJobPosts">
              <IconArrowClockwise />
            </button>
          </div>
          <button
            v-if="profile.accType === 'business'"
            type="button"
            class="btn btn-sm lg:btn-md btn-primary btn-outline"
            @click="showModalJobPost"
          >
            create job post
          </button>
        </div>
      </div>
    </AppHero>
    <AppHero :center="false" :fit="true">
      <template #side>
        <CardJobPostFull
          v-if="jobPosts.length > 0"
          :title="jobPosts[selected].title"
          :location="jobPosts[selected].location"
          :employ-type="jobPosts[selected].employmentType"
          :salary="`$${jobPosts[selected].salaryRange.min} - $${jobPosts[selected].salaryRange.max}`"
          :required-exp="jobPosts[selected].requiredExperience"
          :required-edu="jobPosts[selected].requiredEducation"
          :industry="jobPosts[selected].industry"
          :job-function="jobPosts[selected].function"
          :desc="jobPosts[selected].description"
          :requirements="jobPosts[selected].requirements"
          :benefits="jobPosts[selected].benefits"
          :verify-status="false"
          class="hidden lg:block flex-1 max-h-screen overflow-y-auto"
        />
      </template>
      <div class="job-posts">
        <CardJobPost
          v-if="jobPosts.length > 0"
          v-for="(jobPost, index) in jobPosts"
          :key="jobPost._id"
          :title="jobPost.title"
          :location="jobPost.location"
          :employ-type="jobPost.employmentType"
          :salary="`$${jobPost.salaryRange.min} - $${jobPost.salaryRange.max}`"
          :selected="selected === index"
          :verify-status="false"
          @select="selectJobPost(index)"
        />
      </div>
    </AppHero>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      selected: 0,
      // jobPosts: [
      //   {
      //     title: 'frontend web developer',
      //     business: 'Benefit Solutions Pte Ltd',
      //     location: 'Malaysia',
      //     employmentType: 'internship',
      //     desc: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur illo ut voluptatum omnis soluta corrupti non ad eius cumque rem, quia praesentium exercitationem id qui nulla architecto quis quibusdam ipsam.',
      //   },
      //   {
      //     title: 'backend web developer',
      //     business: 'Benefit Solutions Pte Ltd',
      //     location: 'Malaysia',
      //     employmentType: 'full-time',
      //     desc: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur illo ut voluptatum omnis soluta corrupti non ad eius cumque rem, quia praesentium exercitationem id qui nulla architecto quis quibusdam ipsam.',
      //   },
      // ],
    };
  },
  computed: {
    ...mapGetters('job-posts', ['jobPosts']),
    ...mapGetters('profile', ['profile']),
  },
  methods: {
    ...mapActions('job-posts', ['fetchJobPosts']),
    showModalJobPost() {
      const modalJobPost = document.getElementById('modal-job-post');
      modalJobPost.classList.add('modal-open');
    },
    selectJobPost(id) {
      this.selected = id;
    },
  },
  async fetch() {
    await this.fetchJobPosts();
  },
};
</script>

<style scoped>
:deep(.hero-content) {
  @apply items-start w-full;
}

.job-posts {
  @apply flex flex-col gap-y-6;
}
</style>
