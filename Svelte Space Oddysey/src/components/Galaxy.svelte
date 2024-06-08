<script>
  import Planet from './Planet.svelte';
  import Fleet from './Fleet.svelte';
  import { onMount } from 'svelte';

  let width = 800;
  let height = 600;
  let planets = [];
  let fleets = [];

  function generateGalaxy() {
    planets = [];
    for (let i = 0; i < 20; i++) {
      planets.push({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 20 + 10,
        owner: null,
        resources: Math.floor(Math.random() * 100)
      });
    }
  }

  function addFleet(x, y) {
    fleets.push({ x, y, targetX: Math.random() * width, targetY: Math.random() * height, owner: 'player' });
  }

  onMount(generateGalaxy);
</script>

<svg width={width} height={height} style="border: 1px solid black;" on:click="{e => addFleet(e.offsetX, e.offsetY)}">
  {#each planets as planet}
    <Planet {planet} />
  {/each}
  {#each fleets as fleet}
    <Fleet {fleet} />
  {/each}
</svg>
