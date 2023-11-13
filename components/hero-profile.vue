<template>
  <AppHero :center="false" :main-max-w="false">
    <div class="flex flex-col items-center md:min-w-[28rem]">
      <div class="avatar placeholder mb-6">
        <div class="w-20 lg:w-32 bg-primary text-primary-content rounded-full">
          <span class="text-2xl lg:text-4xl">{{ profile.placeholder }}</span>
        </div>
      </div>
      <h2 class="text-2xl font-semibold text-center" v-html="fullName()"></h2>
    </div>
    <template #side>
      <div class="w-full md:w-auto">
        <div class="tabs">
          <a
            class="app-tab"
            :class="{ 'tab-active': activeTab === 1 }"
            @click="showTab(1)"
            >Account</a
          >
          <a
            class="app-tab"
            :class="{ 'tab-active': activeTab === 2 }"
            @click="showTab(2)"
            >Profile</a
          >
        </div>
        <CardAccount
          v-if="activeTab === 1"
          class="md:w-[28rem] rounded-tl-none"
        />
        <CardProfile v-if="activeTab === 2" class="md:w-[28rem]" />
      </div>
    </template>
  </AppHero>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      activeTab: 1,
    };
  },
  computed: {
    ...mapGetters('profile', ['profile']),
  },
  methods: {
    ...mapActions('profile', ['fetchProfile']),
    hasMiddleName() {
      return this.profile.name.first.length > 1;
    },
    fullName() {
      const name = this.profile.name;
      if (this.profile.accType === 'business') return this.profile.bizName;
      return this.hasMiddleName()
        ? `${name.first}<br/>${name.last}`
        : this.profile.fullName;
    },
    showTab(tab) {
      this.activeTab = tab;
    },
  },
};
</script>

<style scoped>
:deep(.hero-content) {
  /* justify-end as it is reversed */
  @apply w-full md:w-auto items-center lg:items-start justify-end lg:justify-center h-full;
}

:deep(.hero-content > *) {
  @apply flex-initial lg:flex-1;
}

.app-tab {
  @apply tab tab-lifted;
  --tab-bg: hsl(var(--b2));
  --tab-border-color: transparent;
}
</style>
