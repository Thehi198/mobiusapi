// simple JS API displays "hello world"

export default (req, res) => {
    res.status(200).json({ name: 'John Doe' })
  }