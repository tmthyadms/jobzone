<template>
  <AppCard
    :title="title"
    :subtitle-first="business"
    :subtitle-second="location"
    :subtitleBadges="[employType, salary]"
    class="group hover:cursor-pointer transition ease-out"
    :class="{ 'border border-base-content': selected, 'app-border': !selected }"
    @click="$emit('select')"
  >
    <template #icon>
      <div
        class="tooltip tooltip-left font-normal normal-case"
        :class="verifyStatus ? 'tooltip-success' : 'tooltip-gray-400'"
        :data-tip="verifyStatus ? verify.tip : verify.not.tip"
      >
        <button type="button" class="btn btn-xs btn-ghost btn-circle">
          <IconPathCheckFill
            :class="verifyStatus ? 'fill-success' : 'fill-gray-400'"
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
    business: {
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
    verifyStatus: {
      type: Boolean,
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
  @apply before:bg-gray-400 after:border-l-gray-400 before:text-inherit;
}
</style>
