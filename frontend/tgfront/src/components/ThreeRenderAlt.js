import React, { Component } from "react";
import * as THREE from "three";

class SceneAlt extends Component {
  constructor(props) {
    super(props);

    this.start = this.start.bind(this);
    this.stop = this.stop.bind(this);
    this.animate = this.animate.bind(this);
  }

  componentDidMount() {
    const width = this.mount.clientWidth;
    const height = this.mount.clientHeight;
    //scene set up
    const scene = new THREE.Scene();
    const circle = new THREE.Object3D();
    const skelet = new THREE.Object3D();
    const particle = new THREE.Object3D();
    scene.add(circle);
    scene.add(skelet);
    scene.add(particle);
    ///////////////////////////////////

    //camera
    const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    camera.position.set(0, -160, 0);

    ///////////////////////////////////

    //material setup
    var material = new THREE.MeshPhongMaterial({
      color: 0xffffff,
      shading: THREE.FlatShading,
      transparent: true,
      opacity: 0.9
    });
    ///////////////////////////////////

    //geometry setup
    var geometry = new THREE.TetrahedronGeometry(2, 0);
    var geom = new THREE.IcosahedronGeometry(6, 1);
    var geom2 = new THREE.IcosahedronGeometry(15, 1);

    for (var i = 0; i < 1000; i++) {
      var mesh = new THREE.Mesh(geometry, material);
      mesh.position
        .set(Math.random() - 0.5, Math.random() - 0.5, Math.random() - 0.5)
        .normalize();
      mesh.position.multiplyScalar(90 + Math.random() * 700);
      mesh.rotation.set(
        Math.random() * 2,
        Math.random() * 2,
        Math.random() * 2
      );
      particle.add(mesh);
    }
    ///////////////////////////////////

    //inner planet
    var mat = new THREE.MeshPhongMaterial({
      color: 0xffffff,
      shading: THREE.FlatShading
    });

    var planet = new THREE.Mesh(geom, mat);
    planet.scale.x = planet.scale.y = planet.scale.z = 0;
    circle.add(planet); //adding to scene
    ///////////////////////////////////

    //outer planet
    var mat2 = new THREE.MeshPhongMaterial({
      color: 0xffffff,
      wireframe: true,
      side: THREE.DoubleSide
    });

    var planet2 = new THREE.Mesh(geom2, mat2);
    planet2.scale.x = planet2.scale.y = planet2.scale.z = 35;
    skelet.add(planet2); //adding to scene
    ///////////////////////////////////

    //light shit
    var ambientLight = new THREE.AmbientLight(0x888888);
    scene.add(ambientLight); //adding to scene

    var lights = [];
    lights[0] = new THREE.DirectionalLight(0xffa693, 1);
    lights[0].position.set(1, 0, 0);
    lights[1] = new THREE.DirectionalLight(0xe4c1ff, 1);
    lights[1].position.set(0.75, 1, 0.5);
    lights[2] = new THREE.DirectionalLight(0x4b66f6, 1);
    lights[2].position.set(-0.75, -1, 0.5);
    scene.add(lights[0]); //adding to scene
    scene.add(lights[1]); //adding to scene
    scene.add(lights[2]); //adding to scene
    ///////////////////////////////////

    camera.position.z = 400;

    renderer.setClearColor("#3D62FB");
    // renderer.setPixelRatio(window.devicePixelRatio);

    this.scene = scene;
    this.camera = camera;

    this.renderer = renderer;
    this.material = material;
    this.skelet = skelet;
    this.circle = circle;
    this.particle = particle;
    this.mount.appendChild(this.renderer.domElement);
    this.start();
  }

  componentWillUnmount() {
    this.stop();
    this.mount.removeChild(this.renderer.domElement);
  }

  start() {
    if (!this.frameId) {
      this.frameId = requestAnimationFrame(this.animate);
    }
  }

  stop() {
    cancelAnimationFrame(this.frameId);
  }
  resizeCanvasToDisplaySize() {
    const canvas = this.renderer.domElement;
    // look up the size the canvas is being displayed
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;

    // adjust displayBuffer size to match
    if (canvas.width !== width || canvas.height !== height) {
      // you must pass false here or three.js sadly fights the browser
      this.renderer.setSize(width, height, false);
      this.camera.aspect = width / height;
      this.camera.updateProjectionMatrix();

      // update any render target sizes here
    }
  }
  animate() {
    this.particle.rotation.x += 0.0;
    this.particle.rotation.y -= 0.004;
    this.circle.rotation.x -= 0.002;
    this.circle.rotation.y -= 0.003;
    this.skelet.rotation.x -= 0.001;
    this.skelet.rotation.y += 0.002;
    var tanFOV = Math.tan(((Math.PI / 180) * this.camera.fov) / 2);
    var windowHeight = window.innerHeight;
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.fov =
      (360 / Math.PI) * Math.atan(tanFOV * (window.innerHeight / windowHeight));
    this.camera.updateProjectionMatrix();
    this.resizeCanvasToDisplaySize();

    // this.renderer.setSize(window.innerWidth - 18, window.innerHeight);
    this.renderScene();
    this.frameId = window.requestAnimationFrame(this.animate);
  }

  renderScene() {
    this.renderer.render(this.scene, this.camera);
  }

  render() {
    return (
      <div
        className="three"
        // style={{ height: "110vh", width: "10%" }}
        ref={mount => {
          this.mount = mount;
        }}
      />
    );
  }
}

export default SceneAlt;
