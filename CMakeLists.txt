cmake_minimum_required(VERSION 3.13)
project(otcv8-dev)

on:
  push:
    branches: [ master, dev ]
  pull_request:
    branches: [ master, dev ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        build_type: [Release, Debug]
    env:
      BUILD_TYPE: ${{ matrix.build_type }}
    steps:
      - uses: actions/checkout@v2

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential cmake git gcc g++ libboost-all-dev libzip-dev libphysfs-dev

      - name: Install vcpkg from specific commit
        run: |
          git clone https://github.com/microsoft/vcpkg.git
          cd vcpkg
          git checkout 761c81d43335a5d5ccc2ec8ad90bd7e2cbba734e
          ./bootstrap-vcpkg.sh
          cd ..

      - name: Build project
        run: |
          mkdir build
          cd build
          cmake .. -DCMAKE_BUILD_TYPE=${{ env.BUILD_TYPE }}
          make -j8
