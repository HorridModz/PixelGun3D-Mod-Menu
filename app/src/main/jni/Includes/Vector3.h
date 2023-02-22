//Thanks to https://platinmods.com/threads/how-to-make-a-teleport-hack.137887/ for this header

struct Vector3{
  float x;
  float y;
  float z;

  Vector3();
  Vector3(float x, float y, float z);
  ~Vector3();
};

Vector3::Vector3() {}
Vector3::Vector3(float x, float y, float z) : x(x), y(y), z(z) {}
Vector3::~Vector3() {}