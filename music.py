@commands.command(name='play', aliases=['p'])
async def _play(self, ctx: commands.Context, *, search: str):
  if not ctx.voice_state.voice:
    await ctx.invoke(self._join)

  async with ctx.typing():
    try:
      source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
    except YTDLError as e:
      await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
  else:
    song = Song(source)

    await ctx.voice_state.songs.put(song)
    await ctx.send('Enqueued {}'.format(str(source)))

    LLLLLLLLLLLLLLLLLLLLLLLL