<template>
  <div :id="flipIdAttr" class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <slot name="front"></slot>
      </div>
      <div class="flip-card-back">
        <slot name="back"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  expose: ['flip'],
  props: {
    flipId: {
      type: Number,
      default: 0,
    },
    flipName: {
      type: String,
      default: 'def',
    },
    manual: {
      type: Boolean,
    },
  },
  data() {
    return {
      flipIdAttr: null,
    };
  },
  computed: {
    newFlipId() {
      return `flip-card-${this.flipName}-${this.flipId}`;
    },
  },
  created() {
    this.flipIdAttr = this.newFlipId;
  },
  mounted() {
    if (!this.manual) {
      const flipCard = document.getElementById(this.flipIdAttr);
      flipCard.addEventListener('click', this.flip);
    }
  },
  methods: {
    flip() {
      const flipCard = document.getElementById(this.flipIdAttr);
      flipCard.classList.toggle('clicked');
    },
  },
};
</script>

<style scoped>
.flip-card {
  @apply rounded-box;
  perspective: 1000px;
}

.flip-card .flip-card-inner {
  @apply relative w-full h-full rounded-[inherit] transition-transform duration-700;
  transform-style: preserve-3d;
}

.flip-card.clicked .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  @apply rounded-[inherit];
  transform: rotateX(0deg); /* fix for flip card back issue */
  /* ref: https://w3schools.invisionzone.com/topic/59131-flip-card-tutorial-not-working-in-firefox-safari/ */
  backface-visibility: hidden;
}

.fip-card-front {
  @apply relative; /* allow flip card to match front card in size */
}

.flip-card-back {
  @apply absolute top-0 right-0 w-full h-full;
  transform: rotateY(180deg);
}
</style>
