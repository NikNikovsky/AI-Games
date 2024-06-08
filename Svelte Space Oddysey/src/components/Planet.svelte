<script>
    export let planet;
  </script>
  
  <circle cx={planet.x} cy={planet.y} r={planet.size} fill={planet.owner ? 'blue' : 'gray'} />
  