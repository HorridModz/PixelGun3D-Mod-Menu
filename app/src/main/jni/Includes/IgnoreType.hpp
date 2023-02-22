//I made this struct with help from https://en.cppreference.com/w/cpp/utility/tuple/ignore

struct ignoretype {
    template <typename T>
    constexpr // required since C++14
    void operator=(T&&) const noexcept {}
};