# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import asyncio

async def main():
  print('Hello...')
  await asyncio.sleep(1)
  print('... World!')

asyncio.run(main())
