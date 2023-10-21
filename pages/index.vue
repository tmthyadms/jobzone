<template>
  <div class="flex flex-col justify-between min-h-screen">
    <TheHeader />
    <main>
      <AppHero
        title="hero a"
        desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        img="https://placehold.co/1740x1160"
        ><button class="btn btn-primary">get started</button></AppHero
      >
      <AppHero
        title="hero b"
        desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        :center="false"
        figure="https://placehold.co/200x280"
        ><button class="btn btn-primary">learn more</button>
      </AppHero>
      <AppHero
        title="hero c"
        desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        img="https://placehold.co/1740x1160"
        :center="false"
      >
        <AppCard
          title="card a"
          desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          figure="https://placekitten.com/512"
          :overlay="true"
          ><button class="btn btn-primary">learn more</button></AppCard
        >
      </AppHero>
      <AppHero
        title="hero d"
        desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        :center="false"
      >
        <div class="app-flex">
          <AppCard
            title="card a"
            desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
            badge="BADGE"
            figure="https://placehold.co/512"
            :hover="true"
          />
          <AppCard
            title="card b"
            desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
            figure="https://placehold.co/512"
            :hover="true"
            :badges="['Badge 1', 'Badge 2']"
          />
        </div>
      </AppHero>
    </main>
    <TheFooter />
  </div>
</template>
