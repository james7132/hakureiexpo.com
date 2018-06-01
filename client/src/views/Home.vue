<template>
  <b-container>
    <b-table hover :items="items"></b-table>
  </b-container>
</template>

<script>
const items = [
    { name: "Fantasy Crescendo", creator: "Hourai Teahouse", type: "Fangame" },
    { name: "Danmaku!!", creator: "Mystery Parifait", type: "Fangame" },
    { name: "NitorInc: Touhou Microgames", creator: "NitorInc", type: "Fangame" },
    { name: "PC-69 Project", creator: "Pantsu Syndicate", type: "Artbook" },
    { name: "Touhou Orchestral Suite", creator: "crescentia", type: "Music (Album)" },
]

export default {
  data() {
    return {
      items: items
    }
  }
}
</script>
