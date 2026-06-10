
const { createApp } = Vue;

createApp({
  data() {
    // 'data' zijn de variabelen die de pagina gebruikt en laat zien.
    return {
      apiUrl: "http://127.0.0.1:5001",
      goals: [],
      workouts: [],
      progress: null,
      form: {
        week: 4,
        topic: "Push-up en core training",
        reflection: "Ik heb gewerkt aan techniek, controle en een strakkere vorm bij calisthenics.",
      },
      message: "",
      error: "",
      loading: true,
    };
  },
  computed: {
    // Tel hoeveel workouts er zijn.
    totalWorkoutEntries() {
      return this.workouts.length;
    },
  },
  methods: {
    async loadData() {
      // Haal alle informatie van de server op.
      // Eenvoudig uitgelegd: haal de doelen, workouts en voortgang en zet ze op het scherm.
      this.loading = true;
      this.error = "";

      try {
        const [goalsResponse, workoutsResponse, progressResponse] = await Promise.all([
          fetch(`${this.apiUrl}/api/goals`),
          fetch(`${this.apiUrl}/api/workouts`),
          fetch(`${this.apiUrl}/api/progress`),
        ]);

        // Verwerk wat de server stuurde.
        this.goals = await goalsResponse.json();
        this.workouts = await workoutsResponse.json();
        this.progress = await progressResponse.json();
      } catch (error) {
        // Als het ophalen niet lukt, geef een eenvoudige foutmelding.
        // Dit betekent vaak dat de server niet draait (start `python backend/app.py`).
        this.error = "De server antwoordt niet. Start Flask op.";
      } finally {
        this.loading = false;
      }
    },
    async addWorkoutEntry() {
      // Stuur de nieuwe workout naar de server.
      // In gewone woorden: pak wat de gebruiker heeft ingevuld en stuur het naar de backend.
      this.message = "";
      this.error = "";

      try {
        const response = await fetch(`${this.apiUrl}/api/workouts`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            week: Number(this.form.week),
            topic: this.form.topic,
            reflection: this.form.reflection,
          }),
        });

        const result = await response.json();

        if (!response.ok) {
          // Als de server een fout terugstuurt, geef dat als eenvoudige tekst weer.
          throw new Error(result.error || "Kon workout niet toevoegen.");
        }

        // Als het goed ging, voeg de nieuwe workout direct nog even toe aan de pagina.
        this.workouts.push(result);
        this.message = "Workout toegevoegd.";
        // Maak het formulier klaar voor de volgende invoer.
        this.form.week += 1;
        this.form.topic = "";
        this.form.reflection = "";
      } catch (error) {
        this.error = error.message;
      }
    },
  },
  mounted() {
    // Laad alles in als de pagina start.
    this.loadData();
  },
  template: `
    <main class="page-shell">
      <section class="hero">
        <div>
          <p class="eyebrow">Gym & Calisthenics</p>
          <h1>Training Tracker</h1>
        </div>
      </section>

      <!-- Bovenaan zie je cijfers. -->
      <section class="stats" v-if="progress">
        <article>
          <strong>{{ progress.totalGoals }}</strong>
          <span>trainingsdoelen</span>
        </article>
        <article>
          <strong>{{ progress.inProgressGoals }}</strong>
          <span>actief</span>
        </article>
        <article>
          <strong>{{ totalWorkoutEntries }}</strong>
          <span>workouts</span>
        </article>
      </section>

      <p class="status error" v-if="error">{{ error }}</p>
      <p class="status success" v-if="message">{{ message }}</p>
      <p class="loading" v-if="loading">Training data laden...</p>

      <!-- Doelen links, formulier rechts. -->
      <section class="grid">
        <div class="panel">
          <h2>Trainingsdoelen</h2>
          <div class="goal-list">
            <article class="goal-card" v-for="goal in goals" :key="goal.title">
              <div class="goal-header">
                <h3>{{ goal.title }}</h3>
                <span>{{ goal.status }}</span>
              </div>
              <p>{{ goal.description }}</p>
            </article>
          </div>
        </div>

        <div class="panel">
          <h2>Workout toevoegen</h2>
          <form class="form" @submit.prevent="addWorkoutEntry">
            <label>
              Week
              <input type="number" v-model="form.week" min="1" />
            </label>
            <label>
              Workout
              <input type="text" v-model="form.topic" placeholder="Bijvoorbeeld: Push/pull/legs" />
            </label>
            <label>
              Notitie
              <textarea rows="4" v-model="form.reflection" placeholder="Wat heb je getraind en hoe ging het?"></textarea>
            </label>
            <button type="submit">Toevoegen</button>
          </form>
        </div>
      </section>

      <!-- Hieronder zie je alle workouts. -->
      <section class="panel">
        <h2>Workouts</h2>
        <div class="timeline">
          <article class="timeline-item" v-for="item in workouts" :key="item.week + item.topic">
            <div class="timeline-week">Week {{ item.week }}</div>
            <div>
              <h3>{{ item.topic }}</h3>
              <p>{{ item.reflection }}</p>
            </div>
          </article>
        </div>
      </section>
    </main>
  `,
}).mount("#app");
