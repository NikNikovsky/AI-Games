<script>
    export let fleet;
  
    let animationFrame;
  
    function moveFleet() {
      const dx = fleet.targetX - fleet.x;
      const dy = fleet.targetY - fleet.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      if (distance > 1) {
        fleet.x += dx / distance;
        fleet.y += dy / distance;
        animationFrame = requestAnimationFrame(moveFleet);
      } else {
        cancelAnimationFrame(animationFrame);
      }
    }
  
    $: moveFleet();
  </script>
  
  <circle cx={fleet.x} cy={fleet.y} r="5" fill={fleet.owner === 'player' ? 'green' : 'red'} />
  