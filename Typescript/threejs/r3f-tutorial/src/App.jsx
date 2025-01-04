import { Canvas, useFrame } from "@react-three/fiber";
import { useRef } from "react";
import { OrbitControls, GizmoHelper, GizmoViewcube, useHelper} from "@react-three/drei";
import { useControls } from 'leva';
import { SpotLightHelper } from "three";

function LightWithHelper() {
  const light = useRef();

  const { angle, penumbra }  = useControls({
    angle: Math.PI / 8,
    penumbra: {
      value: 0, 
      min: 0,
      max: 1, 
      step: 0.1
    }
  });

  useHelper(light, SpotLightHelper, 'orange');

  return (
     <spotLight 
        castShadow
        ref={light} 
        intensity={80} 
        color={0xffea00} 
        position={[2, 5, 1]} 
        angle={angle}
        penumbra={penumbra}
      />
  )
}

function AnimatedBox() {
  const boxRef = useRef();

  const { color, speed } = useControls({
    color: '#00bfff',
    speed: {
      value: 0.005,
      min: 0,
      max: 0.05,
      step: 0.001,
    },
  });

  useFrame(() => {
    boxRef.current.rotation.x += speed;
    boxRef.current.rotation.y += speed;
    boxRef.current.rotation.z += speed;
  });

  return (
    <mesh ref={boxRef} castShadow>
      <boxGeometry args={[2, 2, 2]} />
      <meshStandardMaterial color={color} />
    </mesh>
  )
}

function App() { 
  return (
    <div id="canvas-container">
      <Canvas shadows>
        <GizmoHelper alignment="bottom-right" margin={[80, 80]}>
          <GizmoViewcube/>
        </GizmoHelper>
        <gridHelper args={[20, 20, 0xff22aa, 0x55ccff]} />
        <axesHelper args={[10]}/>
        <OrbitControls movementSpeed={3}/>
        <AnimatedBox />
        <ambientLight  intensity={0.2} color='oxfcfcfc'/>
        <LightWithHelper />
        <mesh rotation={[-Math.PI / 2, 0, 0]}>
          <planeGeometry args={[20, 20]} />
          <meshStandardMaterial/>
        </mesh>
      </Canvas>
    </div>
  )
};

export default App;
