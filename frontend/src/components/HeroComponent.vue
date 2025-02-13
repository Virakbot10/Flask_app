<template>
  <section class="hero">
    <div class="hero-content">
      <h1>Welcome to DENSO</h1>
      <p>Innovating for a sustainable future</p>
      <button @click="learnMore">Learn More</button>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroComponent',
  methods: {
    learnMore() {
      // Navigate to a detailed section or another page
      window.location.href = '#';
    }
  }
}
</script>

<style scoped>
.hero {
  background-image: url('https://example.com/denso-hero.jpg'); /* Replace with your DENSO-style image */
  background-size: cover;
  background-position: center;
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.hero-content {
  background-color: rgba(255, 255, 255, 0.85);
  padding: 40px;
  text-align: center;
  border-radius: 8px;
}
.hero-content h1 {
  font-size: 48px;
  color: #e60012;
  margin-bottom: 20px;
  font-family: 'DENSO Sans', sans-serif;
}
.hero-content p {
  font-size: 20px;
  color: #333;
  margin-bottom: 30px;
  font-family: Arial, sans-serif;
}
.hero-content button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #e60012;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.hero-content button:hover {
  background-color: #b3000e;
}
</style>
