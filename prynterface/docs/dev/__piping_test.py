from dataclasses import dataclass
import asyncio
import random
#test


class Module1:
    def __init__(self):
        self.data = None
        self.has_data = asyncio.Condition()

    def some_func(self, data: str):
        self.data = data + " Module1 "
        print("Module1 converted data: ", self.data)

    async def add_data(self, data: str):
        print("Module1 adding data: ", data)
        async with self.has_data:
            self.some_func(data)
            self.has_data.notify_all()

    async def generator(self):
        while True:
            async with self.has_data:
                while self.data is None:
                    await self.has_data.wait()
                print("Module1 yielding data: ", self.data, " to M2")
                yield self.data
                self.data = None


class Module2:
    def __init__(self):
        self.data = None
        self.has_data = asyncio.Condition()

    def some_func(self, data: str):
        self.data = data + " Module2 "
        print("Module2 converted data: ", data)

    async def add_data(self, data: str):
        print("Module2 adding data: ", data)
        async with self.has_data:
            self.some_func(data)
            self.has_data.notify_all()

    async def generator(self):
        while True:
            async with self.has_data:
                while self.data is None:
                    await self.has_data.wait()
                print("Module2 yielding data: ", self.data, " to M3")
                yield self.data
                self.data = None


class Module3:
    def __init__(self):
        self.data = None
        self.has_data = asyncio.Condition()

    def some_func(self, data: str):
        self.data = data + " Module3 "
        print("Module3 converted data: ", data)

    async def add_data(self, data: str):
        print("Module3 adding data: ", data)
        async with self.has_data:
            self.some_func(data)
            self.has_data.notify_all()

    async def generator(self):
        while True:
            async with self.has_data:
                while self.data is None:
                    await self.has_data.wait()
                print("Module3 yielding data: ", self.data, " to M4")
                yield self.data
                self.data = None


class Module4:
    def __init__(self):
        self.data = None
        self.has_data = asyncio.Condition()

    def some_func(self, data: str):
        self.data = data + " Module4 "
        print("Module4 converted data: ", data)

    async def add_data(self, data: str):
        print("Module4 adding data: ", data)
        async with self.has_data:
            self.some_func(data)
            self.has_data.notify_all()

    async def generator(self):
        while True:
            async with self.has_data:
                while self.data is None:
                    await self.has_data.wait()
                print("Module4 yielding data: ", self.data, " to M1")
                yield self.data
                self.data = None


class M1Wrapper:
    def __init__(self):
        print("Initializing M1Wrapper")
        self.m1 = Module1()

    def setup(self, generator):
        self.generator = generator

        async def _setup_add():
            print("Setting up M1")
            async for data in self.generator:
                print("M1 got data: ", data, " from random data")
                await self.m1.add_data(data)

        asyncio.create_task(_setup_add())
        return self.m1.generator()


class M2Wrapper:
    def __init__(self):
        print("Initializing M2Wrapper")
        self.m2 = Module2()

    def setup(self, generator):
        self.generator = generator

        async def _setup_add():
            print("Setting up M2")
            async for data in self.generator:
                print("M2 got data: ", data, " from M1")
                await self.m2.add_data(data)

        asyncio.create_task(_setup_add())
        return self.m2.generator()


class M3Wrapper:
    def __init__(self):
        print("Initializing M3Wrapper")
        self.m3 = Module3()

    def setup(self, generator):
        self.generator = generator

        async def _setup_add():
            print("Setting up M3")
            async for data in self.generator:
                print("M3 got data: ", data, " from M2")
                await self.m3.add_data(data)

        asyncio.create_task(_setup_add())
        return self.m3.generator()


class M4Wrapper:
    def __init__(self):
        print("Initializing M4Wrapper")
        self.m4 = Module4()

    def setup(self, generator):
        self.generator = generator

        async def _setup_add():
            print("Setting up M4")
            async for data in self.generator:
                print("M4 got data: ", data, " from M3")
                await self.m4.add_data(data)

        asyncio.create_task(_setup_add())
        return self.m4.generator()


async def random_data():
    await asyncio.sleep(2)
    while True:
        num = random.randint(99999, 10000000)
        data = f"Random Data #{num}"
        print(f"Sending {data}")
        yield data
        await asyncio.sleep(random.randint(1, 5))


class Pipeline:
    """A pipeline of modules."""

    def __init__(self, modules: list):
        self.modules = modules

    def setup(self):
        generator = random_data()
        for module in self.modules:
            generator = module.setup(generator)
        return generator


async def main():
    m1 = M1Wrapper()
    m2 = M2Wrapper()
    m3 = M3Wrapper()
    m4 = M4Wrapper()
    pipeline = Pipeline([m1, m2, m3, m4])
    generator = pipeline.setup()
    async for data in generator:
        print("Final data:", data)


asyncio.run(main())
