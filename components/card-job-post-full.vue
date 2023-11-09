<template>
  <AppCard
    :title="title"
    :subtitle-first="businessName"
    :subtitle-second="location"
    :subtitleBadges="[employType, salary]"
    :desc="desc"
    class="app-border bg-base-200"
  >
    <template #icon>
      <div
        class="tooltip tooltip-left font-normal normal-case"
        :class="isFraudulent ? 'tooltip-gray-400' : 'tooltip-success'"
        :data-tip="isFraudulent ? verify.not.tip : verify.tip"
      >
        <button type="button" class="btn btn-xs btn-ghost btn-circle">
          <IconPathCheckFill
            :class="isFraudulent ? 'fill-gray-400' : 'fill-success'"
          />
        </button>
      </div>
    </template>
    <template>
      <div class="divider"></div>
      <div class="space-y-6">
        <div class="flex">
          <div class="flex-1">
            <p class="text-xs font-semibold capitalize opacity-60">
              experience
            </p>
            <p class="text-sm">{{ requiredExp }}</p>
          </div>
          <div class="flex-1">
            <p class="text-xs font-semibold capitalize opacity-60">education</p>
            <p class="text-sm">{{ requiredEdu }}</p>
          </div>
        </div>
        <div class="flex">
          <div class="flex-1">
            <p class="text-xs font-semibold capitalize opacity-60">industry</p>
            <p class="text-sm">{{ industry }}</p>
          </div>
          <div class="flex-1">
            <p class="text-xs font-semibold capitalize opacity-60">function</p>
            <p class="text-sm">{{ jobFunction }}</p>
          </div>
        </div>
        <div>
          <p class="text-xs font-semibold capitalize opacity-60">
            requirements
          </p>
          <p class="text-sm">{{ requirements }}</p>
        </div>
        <div>
          <p class="text-xs font-semibold capitalize opacity-60">benefits</p>
          <p class="text-sm">{{ benefits }}</p>
        </div>
      </div>
    </template>
    <template #action>
      <div class="space-x-2">
        <div class="tooltip tooltip-left align-bottom" data-tip="Report job">
          <button class="btn btn-error btn-outline">
            <IconFlagFill />
          </button>
        </div>
        <button v-if="profile.accType === 'job-seeker'" class="btn btn-primary">
          apply now
        </button>
      </div>
    </template>
  </AppCard>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      verify: {
        tip: 'This job post is verified by our system and has a high likelihood of being good for you.',
        not: {
          tip: "Our system couldn't successfully verify this job post. Please be careful when applying.",
        },
      },
    };
  },
  props: {
    title: {
      type: String,
    },
    businessName: {
      type: String,
    },
    location: {
      type: String,
    },
    employType: {
      type: String,
    },
    salary: {
      type: String,
    },
    requiredExp: {
      type: String,
    },
    requiredEdu: {
      type: String,
    },
    industry: {
      type: String,
    },
    jobFunction: {
      type: String,
    },
    desc: {
      type: String,
    },
    requirements: {
      type: String,
    },
    benefits: {
      type: String,
    },
    fraudulent: {
      type: Number,
    },
  },
  computed: {
    ...mapGetters('profile', ['profile']),
    isFraudulent() {
      return this.fraudulent === 1;
    },
  },
};
</script>

<style scoped>
.tooltip-gray-400 {
  @apply before:bg-gray-400 after:border-l-gray-400 before:text-inherit;
}

:deep(.card-actions) {
  @apply justify-end;
}
</style>
