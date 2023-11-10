<template>
  <AppCard
    :title="title"
    :subtitle-first="businessName"
    :subtitle-second="location"
    :subtitleBadges="[employType, salary]"
    class="group hover:cursor-pointer transition ease-out"
    :class="{ 'border border-base-content': selected, 'app-border': !selected }"
    @click="$emit('select')"
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
  </AppCard>
</template>

<script>
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
    selected: {
      type: Boolean,
    },
    fraudulent: {
      type: Number,
    },
  },
  computed: {
    isFraudulent() {
      return this.fraudulent === 1;
    },
  },
};
</script>

<style scoped>
:deep(.card-title) {
  @apply group-hover:underline;
}

:deep(.card-subtitle) {
  @apply opacity-60;
}

.tooltip-gray-400 {
  @apply before:bg-gray-400 after:border-l-gray-400 before:text-neutral;
}
</style>
