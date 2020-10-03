  <template>
    <div class="center examplex">
      <vs-navbar center-collapsed v-model="active">
        <template #left>
          <img src="@/assets/logo-wide.png" alt="" style="height:28px;">
        </template>
        <vs-navbar-item :active="active == 'guide'" id="guide">
          Home
        </vs-navbar-item>
        <vs-navbar-item :active="active == 'docs'" id="docs">
          About
        </vs-navbar-item>
        <vs-navbar-item :active="active == 'components'" id="components">
          Software
        </vs-navbar-item>
        <vs-navbar-item :active="active == 'license'" id="license">
          3D Printing
        </vs-navbar-item>
        <template #right>
          <vs-button
        circle
      >Contact
      </vs-button>

        </template>
      </vs-navbar>
    </div>
  </template>

  <script>
export default {
  name: "Nav",
  data: () => ({
    active: "guide",
  }),
};
</script>